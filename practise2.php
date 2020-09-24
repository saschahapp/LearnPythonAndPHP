<?php
if (!empty($_POST['zahl'])) {
    print "Ihre Eingabe wurde erfasst und für die Berechnung des neuen Dokuments verwendet.";
    $handle = fopen("practise.txt", "r");
    $handle2 = fopen("practise2.txt", "w");
    $ergebnis = array();
    if ($handle) {
        $i = 0;
        while (!feof($handle)) {
            $inhalt = fgets($handle);
            $ergebnis[$i] = $inhalt;
            $i++;
        }
        if ($_POST['zahl'] != "") {
            $faktor = $_POST['zahl'];
            foreach ($ergebnis as $wert) {
                $wert = intval($wert)*$faktor;
                fputs($handle2, $wert."\n");
            }
        }
        fclose($handle);
        fclose($handle2);    
    }
    else {
        print "Die Datei konnte nicht geöffnet werden!\n";
    }
}
?>

