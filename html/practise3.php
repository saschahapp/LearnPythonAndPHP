<?php
$sql = "INSERT INTO os_bestellungen (b_artikelnummer, b_kundennummer, b_preis, b_anzahl) VALUES (1011, 2001, 45.99, 1);";
$sql2 = "DELETE FROM os_bestellungen WHERE b_id = 1;";
$sql3 = "UPDATE os_bestellungen SET b_anzahl = b_anzahl + 1 WHERE b_id = 2;";
try {
    $dbh = new PDO ("mysql:dbname=; host=", "", ""); 
    print "Verbindung erfolgreich hergestellt.";
    $dbh->query($sql3);
    $error = $dbh->errorInfo();
    if ($error[0] > 0) {
        print "Fehlercode: ".$error[1]."<br>".$error[2];
    }
    $dbh = null;
}
catch(PDOException $e) {
    print $e->getMessage();
}
?>
