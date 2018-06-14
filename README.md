# kquery
Damn light QT based database client

This postgresql client is inteded to please KDE Plasma users who use realy low specs hardware (Yepo laptops, Raspberry PI, etc), who already runs Plasma or QT desktop and don't want fancy resources wich full database IDEs avalaible like DBeaver  already provide.

The goal is to keep light, quick opening, usable tiny interface with basic database features for software developers.

If you need complicated database management features, have a decent modern workstation or don't use a Plasma/QT desktop, this is not the tool for you, there are plenty other wonderfull clients out there.

Bonus feature: funny dialogs for user interaction.

## FAQ
Q - Why did you chose PyQt5, a 100+MB framework for a "light" database client? You must be stupid to load that much dependency for such a small application.

A - Because this amount of space isn't a problem for me. Hard Disk space is plenty available and cheap nowadays, not as much as battery/memmory/processing in low powered devices.

Q - Do you plan to provide other database connectors? Or improved postgresql connecion features?

A - Yes! If I have enougth time and application load time and performance is not compromised, why not?