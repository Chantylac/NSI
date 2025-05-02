<!-- =================================================== PHP =================================================== -->
<?php
  session_start(); // Démarre une session PHP pour stocker des données

  date_default_timezone_set("Europe/Paris"); // Définit le fuseau horaire pour toutes les fonctions date/heure

  // Déclaration des variables de base
  $prix_jeu = "19,99"; // oui le prix est mis en string, non ce n'est pas important
  $place_adulte = 39.99;
  $place_enfant = 19.99;
  $prix_total_adulte = 0;
  $prix_total_enfant = 0;
  $client_statut = "Normal"; // Statut du client par défaut
  $heure_act = date("H"); // Récupère l'heure actuelle en format 24h
  $statut = ""; // Statut d'ouverture du parc
  $adresse_url = 'https://maps.app.goo.gl/EcVMiPnzhziNMubUA'; // Lien vers l’adresse du parc

  // Détermine si le parc est ouvert ou fermé en fonction de l'heure actuelle
  if ($heure_act >= 10 && $heure_act < 20) {
    $statut = "Ouvert";
  } else {
    $statut = "Fermé";
  }

  // Récupère le type de formulaire soumis (identité ou billetterie), ou une chaîne vide si non défini
  $form_type = $_POST["form_type"] ?? '';
  // de plus, ce format est une sorte d'abbréviation de la fonction if:
  // form_type = $_post... s'il existe, sinon il renvoie une chaine de caractère vide


  // Si le formulaire d'identité est soumis et contient un prénom et un nom valides
  if ($form_type === "identite" && !empty($_POST["nom"]) && !empty($_POST["prenom"])) {
    $_SESSION["acces_autorise"] = true; // Autorise l'accès à la billetterie
    $_SESSION["nom"] = $_POST["nom"];
    $_SESSION["prenom"] = $_POST["prenom"];
  }

  // Récupération des données de session (nom, prénom, autorisation)
  $acces_autorise = $_SESSION["acces_autorise"] ?? false;
  $nom = $_SESSION["nom"] ?? '';
  $prenom = $_SESSION["prenom"] ?? '';

  // Si le client correspond à une personne privilégiée, on applique le tarif Golden
  if (($prenom === "Timothé" && $nom === "Sauvage") || ($prenom === "Arthur" && $nom === "Da Silva")) {
    $prix_jeu = "1,99"; // Prix réduit pour le jeu
    $client_statut = "Golden";
  }

  // Si le formulaire billetterie est soumis, traitement de la commande
  if ($form_type === "billetterie") {
    // Récupération des quantités de billets adultes/enfants
    $n_place_adulte = intval($_POST["nAdultes"] ?? 0);
    $n_place_enfant = intval($_POST["nEnfants"] ?? 0);
    $pass = $_POST["pass"] ?? "pass_normal"; // Pass sélectionné

    // Calcul du multiplicateur selon le type de pass
    $multiplicateur = 1;
    if ($pass === "pass_speedy") {
      $multiplicateur = 2;
    } elseif ($pass === "pass_max_speedy") {
      $multiplicateur = 4;
    }

    // Application d'une réduction si le client est "Golden"
    $reduction = ($client_statut === "Golden") ? 0.6 : 1;
    // Golden = -40% donc on multiplie par 0.6

    // Calculs des prix totaux
    $prix_total_adulte = $place_adulte * $n_place_adulte * $multiplicateur * $reduction;
    $prix_total_enfant = $place_enfant * $n_place_enfant * $multiplicateur * $reduction;
    $prix_total = $prix_total_adulte + $prix_total_enfant;
  }
?>


<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Legacy Of Light : Le Parc</title>
  <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet"> <!-- le href ici permet d'acceder aux font de l'api de google-->
</head>
<!-- =================================================== CSS =================================================== -->
<style>


  /* Variables CSS  */
:root {
  --couleur-border-vert: #4b7d2b;
  --couleur-fond-vert: #b3d89d;
  --couleur-3: #f2e1a1;
  --couleur-fond-marron: #c8a95f;
  --coulor-border-marron: #a45e32;
  } 
  html { /* Avoir une direction vers les parties basses du site non instantanée */ 
    scroll-behavior: smooth;
  }
  body{
    font-family: 'Roboto';
    background: linear-gradient(var(--couleur-3),rgb(239, 213, 119)); /*Dégradé du haut vers le bas, créant un effet de profondeur (je trouve) */
  }
  .no-underline a{ /**Pour la balise <a> retirer le soulignage */
    text-decoration: none;
  }
  .navig{
    display: flex;
    justify-content: space-evenly;
    align-content: stretch;
    background-color: var(--couleur-fond-vert);
    border-style:solid;
    border-width: 3px;
    border-color: var(--couleur-border-vert);
    width: device-width;
    height: 64px;
    align-items: center;
    margin-top: 1%;
    padding: 0.2%;
    font-size: 20px;
    margin-left: 1em;
    margin-right: 1em;
  }
  .nav-items{
    list-style: none;
    display: flex;
    align-items: center;
    gap: 4em;
    font-weight:bolder;
    font-size: larger;
    font-family:'Times New Roman';
    
  }
  .nav-items a{/**Pour la balise <a> retirer le soulignage */
    color: black;
    text-decoration: none;
  }
  .nav-items a:hover {/**Pour la balise <a> quand on passe la souris dessus */
   color: #4c2762;
  }
  .nav-bg{
    background-color: rgba(42, 42, 42, 0.3);
    padding: 16px 24px;
    border-radius: 14px;
  }


  .box-infos1, .box-accueil1, .box-billetterie1, .box-jeux1{/**Empilage des classes pour ne pas avoir à les faire plusieurs fois pour rien */
    background-color: var(--couleur-fond-marron);
    border-color: var(--coulor-border-marron);
    border-style: solid;
    border-width: 3px;
    border-radius: 1em;
    padding-left: 10px;
    padding-right: 10px;
    margin-top: 10px;
    padding-top: 10px;
    height: 25em;
    font-size: 20px;
    margin-left: 1em;
    margin-right: 1em;
  }
  .box-accueil-titre, .box-infos-titre, .box-billetterie-titre, .box-jeux-titre{
    background-color: rgba(0, 0, 0, 0.1);
    border-top-right-radius: 3em;
    border-bottom-right-radius: 3em;
    padding-left: 1%;
    border-style:solid;
    border-width: 1%;
    border-color: rgba(0, 0, 0, 0.1);
    justify-items: left;
  } 
  .boxinfoaccueil{
    display: flex;
    gap: 0.5em;
    justify-content: center;
    align-items: flex-start;
  }

  .box-infos1{
    width: 33%;
  }
  .infos-contenu {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    padding: 0.1em ;
  }

  .infos-message {
    width: 90%;
    background-color: rgba(255,255,255,0.3);
    border-color: rgba(0, 0, 0, 0.1);
    border-style: solid;
    border-width: 1%;
    padding: 0.5em;
    border-radius: 2em;
    box-shadow: 0 0 5px rgba(0,0,0,0.1);
  }


  .box-accueil1{
    width: 67%;
  }
  .box-in-accueil{
    display: flex;
    gap: 1em;
    align-items: flex-start;
    justify-content: center;
    background-color: rgba(255,255,255,0.3);
    padding: 1em;
    border-radius: 3em;
    border: solid rgba(0, 0, 0, 0.1);
    border-width: 1%;
  }
  .image-accueil{
    width: 100%;
    height: auto;
    object-fit: contain;
    display: block;
    border-radius: 8px; 
  }

  .box-billetterie-titre{
    margin-bottom: 10px
  }
  .box-in-billetterie{
    display: flex;
    gap: 2em;
    justify-content: space-between;
    align-items: flex-start;
    padding: 1em 0;
  }
  .box-billets{
    background-color: rgba(255,255,255,0.2);
    border-top-left-radius: 2em;
    border-bottom-left-radius: 2em;
    padding-left: 1%;
    border-style:solid;
    border-width: 1%;
    border-color: rgba(0, 0, 0, 0.1);
    height: 16.8em;
  }
  .billetterie-message{
    width: 60%;
    background-color: rgba(255,255,255,0.2);
    border-color: rgba(0, 0, 0, 0.1);
    border-style: solid;
    border-width: 1%;
    padding: 1em;
    border-top-right-radius: 2em;
    border-bottom-right-radius: 2em;
    box-shadow: 0 0 5px rgba(0,0,0,0.1);
    height: 15em;
  }
  .billetterie-form{
    width: 60%;
  }
    .billetterie-message-golden {
    background-color: rgba(255, 223, 0, 0.1);
    border-left: 5px solid #FFD700;
    padding: 1em;
    border-top-right-radius: 2em;
    border-bottom-right-radius: 2em;
  }
  .billetterie-message-normal {
    background-color: rgba(173, 216, 230, 0.1);
    border-left: 5px solid var(--couleur-border-vert);
    padding: 1em;
    border-top-right-radius: 2em;
    border-bottom-right-radius: 2em;
  }
  .prix-calcule, .multiplicateur, .prix-total {
    margin-top: 0.3em;
    color: lightgray;
    font-style: italic;
  }
  .box-jeux1{
    margin-bottom: 100px;
  }
  .box-in-jeux {
    display: flex;
    gap: 2em;
    justify-content: space-between;
    align-items: flex-start;
    padding: 1em 0;
  }

  .jeux-message {
    width: 80%;
    background-color: rgba(255,255,255,0.2);
    border-color: rgba(0, 0, 0, 0.1);
    border-style: solid;
    border-width: 1%;
    padding: 1em;
    border-top-right-radius: 2em;
    border-bottom-right-radius: 2em;
    box-shadow: 0 0 5px rgba(0,0,0,0.1);
  }

  .jeux-image {
    max-width: 90%;
    border-radius: 2em;
    box-shadow: 0 0 5px rgba(0,0,0,0.2);
  }
  
  .button-payer {
  background-color: rgba(255, 255, 255, 0);
  color: black;
  padding: 10px 20px;
  border: none;
  border-radius: 8px;
  font-size: 1em;
  transition: background-color 0.3s ease;
  margin-left: 2em;
}

  .button-payer:hover {
    background-color: rgba(0, 0, 0, 0.1);
  }

  .statut-ouvert{
    color: green;
    font-weight: bold;
  }
  .statut-ferme{
    color:red;
    font-weight: bold;
  }
  

  .box-nom, .box-prenom{
    font-size: 16px;
  }
  input::placeholder{/**Pour la balise <input> mettre en indication les noms par exemple */
    color: rgb(24, 24, 24);;
    font-style: italic;
    opacity: 0.6;
  }
  .form-identite {
    display: flex;
    flex-direction: column;
    gap: 0.5em;
    max-width: 300px; 
    padding-left: 7em;
    padding-top: 1em;
  }
  .form-ligne {
    display: flex;
    align-items: center;
    gap: 0.5em;
  }
  .form-ligne label {
    min-width: 80px;
  }
  .form-ligne input {
    flex: 1;
    padding: 6px;
    border-radius: 5px;
    border: 1px solid var(--couleur-border-vert);
    background-color: var(--couleur-fond-marron);
    background-color: rgba(255, 255, 255, 0.5);
  }
  .form-ligne input[type=submit]{/**Pour la balise <input type="submit">  */
    background-color:var(--couleur-fond-vert)
  }
  .form-ligne input[type=submit]:hover{/**Pour la balise <input type="submit"> si on passe la souris dessus  */
    background-color: rgba(0, 0, 0, 0.1);
  }


  footer {
    position: fixed;/**La position du footer est fixée en bas à gauche pour bouger tout le temps avec nous */
    bottom: 0;
    left: 0;
    width: 100%;
    text-align: center; 
    padding: 1em; 
    background-color: #b3d89d; 
    color: #333; 
    font-size: 0.9em;
    border-top: 3px solid var(--couleur-border-vert);
    box-shadow: 0 -10px 5px rgba(0,0,0,0.2);
    transition: 0.5s ease;
  }/** la transition permet de cacher (ici) le footer ou du moins en partie quand on passe la souris dessus*/
  footer:hover {
    bottom: -40px;
  }
  
</style>
<!-- Par Arthur et Timothé (il faut bien se mettre d'accord sur le style intégral du site)-->
<!-- =================================================== HTML =================================================== -->

<nav class="navig">
  <ul class="nav-items">
    <li class="nav-bg"> <a href="#Accueil">Accueil</a> </li>
    <li class="nav-bg"> <a href="#infos" target="_self">Informations</a> </li>
    <li class="nav-bg"> <a href="#billetterie" target="_self">billetterie</a> </li>
    <li class="nav-bg"> <a href="#jeux" target="_self">Acheter le jeu</a> </li>
  </ul>
</nav>
<!-- Par Timothé -->

<body>
  <div class="boxinfoaccueil">
    <div class="box-accueil1">
      <h2 id="Accueil" class="box-accueil-titre">Accueil</h2>
      <div class="box-in-accueil">
        <div>
          <p>
            Bienvenue sur le site du parc d'attraction du thème de Legacy Of Light&COPY;, le jeu phare du moment !<br>
            Avant d'accéder à d'autres fonctionnalités, vous serez priés de renseigner des informations ci-dessous :<br>
          </p>
          <div>
            <form method="post" class="form-identite" action="">
              <input type="hidden" name="form_type" value="identite">
              <div class="form-ligne">
                <label>Nom :</label>
                <input type="text" id="nom" name="nom" placeholder="Dautremont, Dufeux...">
              </div>
              <div class="form-ligne">
                <label>Prénom :</label>
                <input type="text" id="prenom" name="prenom" placeholder="Mattéo, Léo...">
              </div>
              <div class="form-ligne">
                <input type="submit">
              </div>
            </form>
          </div>
        </div>
      <div>
        <img src="image-7A-ilSpW-hecSWYtPqc6n.png" class="image-accueil">
      </div>
    </div>
  </div>
<!-- Par Timothé -->  

    <div class="box-infos1">
      <h2 id="infos" class="box-infos-titre">Informations</h2>
      <div class="infos-contenu">
        <div class="infos-message">
          <p>
            Voici des informations qui pourraient vous être utiles :
          </p>
          <ul type="circle">
            <li class="no-underline">
              Adresse :
              <a href="<?php echo $adresse_url ?>" target="_blank">
                Rue de Derrière les Mines, 08440 Lumes
              </a>
            </li><br>
            <li>Téléphone : 06 23 41 44 03</li><br>
            <li>
              <?php
                if ($statut == "Ouvert") {
                  echo 'Horaires : <span class="statut-ouvert">' . $statut . '</span> - Ferme à 20:00';
                } else {
                  echo 'Horaires : <span class="statut-ferme">' . $statut . '</span>';
                }
              ?>
            </li><br>
            <li>Restaurants et hôtels dans le parc</li><br>
            <li>Plein de boutiques souvenirs</li><br>
          </ul>
        </div>
      </div>
    </div>
<!-- Par Arthur -->
  </div>

  <?php if($acces_autorise):?>
      <div class="box-billetterie1">
        <h2 id="billetterie" class="box-billetterie-titre"> Billetterie</h2>
        
        <div class="box-in-billetterie">
          <div class="billetterie-message">
            <?php if($client_statut == "Golden"):?>
              <div class="billetterie-message-golden">
                🎉 Bienvenue, <?php echo $prenom; ?> !
                  Vous êtes un client Golden ✨<br>
                  Grâce à votre statut privilégié, vous profitez d’une réduction de 40% sur toutes vos places !<br>
                  Profitez-en pour choisir un pass plus rapide et vivre l'expérience ultime 🚀<br>
              </div>
            <?php else:?>
              <div class="billetterie-message-normal">
                Bonjour <?php echo $prenom; ?>,<br>
                Vous êtes sur le point de vivre une aventure inoubliable dans notre parc !<br>
                Choisissez un pass pour moduler votre vitesse d’accès aux attractions :<br>
                    <br>
                    <strong>Normal :</strong> Un accès lent, mais à toutes les attractions !<br>
                    <br>
                    <strong>Speedy :</strong> une seule fois en un instant !<br>
                    <br>
                    <strong>Max Speedy :</strong> accédez partout en un éclair !<br>
                    <br>
                Les tarifs varient selon le pass sélectionné.
            </div>
            <?php endif?>
          </div>
          <div class="billetterie-form">
            <form method="post" action="#billetterie">
              <input type="hidden" name="form_type" value="billetterie">
              <div class="box-billets">
                <p>
                  <label> Nombre d'adultes (+12 ans) [39.99€]</label>
                  <input type="number" size="2" name="nAdultes" min="0" placeholder="0">
                  <p class="prix_calcule
                  ">Total adultes : <?php echo $prix_total_adulte ?> €<br></p>
                  <label> Nombre d'enfants (-12 ans) [19.99€]</label>
                  <input type="number" size="2" name="nEnfants" min="0" placeholder="0">
                  Total enfants : <?php echo $prix_total_enfant ?> €<br>
                </p>
              <p>               
                  <label> Pass </label>
                  <select size="1" name="pass">
                    <option value="pass_normal"> Normal </option>
                    <option value="pass_speedy"> Speedy </option>
                    <option value="pass_max_speedy"> Max Speedy </option>
                  </select>
                  Multiplicateur : <?php echo "x"+$multiplicateur ?>
                </p>
                
                <p>Total à payer : <?php echo number_format($prix_total, 2); ?> €</p>
              
                <p>
                  <input type="submit" value="Calculer">
                </p>
              </div>
            </form>
          </div>
        </div>
<!-- Par Arthur -->

        
      </div>
      <div class="box-jeux1">
        <h2 id="jeux" class="box-jeux-titre">Notre jeu vidéo : Legacy Of Light</h2>
        <div class="box-in-jeux">  
          <div class="jeux-message">
            Plongez dans l’univers de <strong>Legacy Of Light</strong>, notre jeu exclusif !<br><br>
            Retrouvez l’ambiance du parc chez vous avec ce jeu captivant d’aventure et de stratégie.<br>
            <br>
            Prix spécial : <strong><?php echo $prix_jeu ?>€</strong>
            <a href="https://github.com/Chantylac/NSI/releases/tag/v1.0" target="_blank">
              <button class="button-payer">Payer maintenant</button>
            </a>
            <br><br>
            Disponible uniquement sur notre site. Ne ratez pas l’occasion de prolonger l’expérience <br>
            
          </div>
          <div>
            <img class="jeux-image" src="LoLcover.jpg"></>
          </div>
        </div>
      </div>
    <?php endif?>

    <footer class="footer-repliable">
      © 2025 Legacy Of Light. Tous droits réservés.
    </footer>
<!-- Par Timothé -->
  
</body>
</html>