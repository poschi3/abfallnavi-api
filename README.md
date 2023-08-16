# abfallnavi API

Zugriff auf die Termine der Müllabfuhr.

Die Firma [regio iT](https://www.regioit.de) bietet für diverse Kommunen die Software [abfallnavi](https://www.regioit.de/produkte-leistungen/sap-loesungen/entsorgung/abfallapp-abfallnavi) an.


## Bekannte Kommunen:

* [Aachen](https://serviceportal.aachen.de/abfallnavi)
* [AWA Entsorgungs GmbH](https://abfallkalender.regioit.de/abfall-webapp-awa/)
* [Bergisch Gladbach](https://www.bergischgladbach.de/abfuhrbezirksabfrage.aspx)
* [Bergischer Abfallwirtschaftverbund](https://www.bavweb.de/Bergischer-Abfallwirtschaftsverband/Einsammeln-und-Transportieren-in-/Engelskirchen/)
* [Dinslaken](https://www.dinslaken.de/de/dienstleistungen/abfall-navi/)
* [Dorsten](https://www.ebd-dorsten.de/)
* [Gütersloh](https://buergerportal.guetersloh.de/abfallkalender)
* [Halver](https://www.halver.de/2014/rathaus_politik/abfall/abfallkalender/index.php)
* [Kreis Coesfeld](https://www.wbc-coesfeld.de/service/abfall-infos-ihrer-stadt-gemeinde.html)
* [Kreis Heinsberg](https://abfallnavi.de/heinsberg/)
* [Kreis Pinneberg](https://abfall.kreis-pinneberg.de/Service+_+Termine/Abfuhrtermine+%28alle+Orte%29.html)
* [Kreis Warendorf](https://abfallnavi.de/krgt/)
* [Lindlar](https://www.lindlar.de/buergerinfo-und-service/abfallentsorgung.html)
* [Lüdenscheid](https://www.stl-luedenscheid.de/abfallnavi)
* [Norderstedt](https://www.betriebsamt-norderstedt.de/Abfall/Service/Abfall-App/)
* [Nürnberg](https://www.nuernberg.de/internet/abfallwirtschaft/abfallkalender_app.html)
* [Roetgen](https://buergerportal.roetgen.de/abfallnavi)
* [Solingen](https://www.solingen.de/tbs/inhalt/abfallnavi/)
* [EGW Westmünsterland](https://www.egw.de/service/abfallberatung/abfallappwestmunsterland/)

Weitere potentielle Kommunen:
* https://ozg.kdn.de/loesungen/details/abfallnawi


# Benutzungshinweis

Für die Abfrage von Terminen ist eine Reihe von IDs (von Orten, Straßen und/oder Hausnummern) in Erfahrung zu bringen. 
**Vorsicht**:*IDs können sich mit der Zeit ändern*

1. Orte aus System holen (z.B. https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest/orte);
2. Mit Ort die Straßen abfragen (z.B. https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest/orte/$ortId/strassen);
3. Mit Straße die Hausnummern abfragen (z.B. https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest/orte/$ortId/strassen/$strassenId);
4. Mit Haunummer die möglichen Fraktionen (Müllsorten) abfragen (z.B. https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest/hausnummern/$hausnummernId/fraktionen);
5. Mit Hausnummer alle Termine abrufen (z.B. https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest/hausnummern/$hausnummernId/termine). Manchmal wird nicht nach Hausnummer unterschieden (z.B. https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest/strassen/$strassenId/termine).
    
## Beispiel
```bash
ortId=$(curl -s https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest/orte | jq '.[0].id');
strassenId=$(curl -s https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest/orte/$ortId/strassen | jq '.[] | select(.name == "Aachener Strasse").id');
hausnummernId=$(curl -s https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest/orte/$ortId/strassen/$strassenId | jq '.[] | select(.name=="Aachener Strasse").hausNrList | .[] | select(.nr=="1").id');
fraktionsId=$(curl -s https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest/fraktionen | jq '.[] | select(.name=="Restabfall").id');
fraktionsId2=$(curl -s https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest/hausnummern/$hausnummernId/fraktionen | jq '.[] | select(.name=="Restabfall").id');
fraktionsId3=$(curl -s https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest/strassen/$strassenId/fraktionen);
termine=$(curl -s https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest/strassen/$strassenId/termine);
termine2=$(curl -s https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest/hausnummern/$hausnummernId/termine);
```
