<?php
    $handle = fopen("daten.txt", "a");
    if ($handle) { 
        if (!empty($_POST['name']) && !empty($_POST['e-mail'])) { 
            if (filter_var($_POST['e-mail'], FILTER_VALIDATE_EMAIL) && preg_match("/^([a-zA-Z' ]+)$/", $_POST['name'])) {
                if (!empty($_POST['name'])) { 
                    fwrite($handle, $_POST['name']."\n");
                }
                if (!empty($_POST['e-mail'])) { 
                    fwrite($handle, $_POST['e-mail']."\n");           
                }
                print "Vielen Dank für deine Daten!";
            }
            else {
                print "Netter Versuch!";
            }
            fclose($handle);
        }
    }
    else {
        print "Die Datei konnte nicht geöffnet werden.\n";
    }
?>
