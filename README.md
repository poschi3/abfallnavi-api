# abfallnavi API

Zugriff auf die Termine der Müllabfuhr.

Die Firma [regio iT](https://www.regioit.de) bietet für diverse Kommunen die Software [abfallnavi](https://www.regioit.de/produkte-leistungen/sap-loesungen/entsorgung/abfallapp-abfallnavi) an.


## Bekannte Komunen:

* [Aachen](https://serviceportal.aachen.de/abfallnavi)
* [AWA Entsorgungs GmbH](https://abfallkalender.regioit.de/abfall-webapp-awa/)
* Bergisch Gladbach
* Bergischer Abfallwirtschaftverbund
* Dinslaken
* Dorsten
* Gütersloh
* Halver
* Kreis Coesfeld
* Kreis Heinsberg
* Kreis Pinneberg
* [Kreis Warendorf](https://abfallnavi.de/krgt/)
* Lindlar
* Lüdenscheid
* Norderstedt
* [Nürnberg](https://www.nuernberg.de/internet/abfallwirtschaft/abfallkalender_app.html)
* Roetgen
* EGW Westmünsterland

Weitere potentielle Kommunen:
* https://ozg.kdn.de/loesungen/details/abfallnawi


# Benutzungshinweis

1. Orte aus System holen (z.B. https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest/orte);
2. Mit Ort die Straßen abfragen (z.B. https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest/orte/4407686/strassen);
3. Mit Straße die Hausnummern abfragen (z.B. https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest/orte/4407686/strassen/4455730);
4. Mit Haunummer die möglichen Fraktionen (Müllsorten) abfragen (z.B. https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest/hausnummern/4407696/fraktionen);
5. Mit Hausnummer alle Termine abrufen (z.B. https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest/strassen/4455730/termine).
    
Manchmal wird nicht nach Hausnummer unterschieden.
    
## Beispiel
```bash
result=$(curl -m 60 https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest/strassen/4455730/termine)
```
