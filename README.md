# kquery
Damn light QT-based database client

[![Build Status](https://travis-ci.org/SamambaMan/kquery.svg?branch=master)](https://travis-ci.org/SamambaMan/kquery)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0ecd8cef49ce4c1aab239b21fff66fc6)](https://www.codacy.com/app/SamambaMan/kquery?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=SamambaMan/kquery&amp;utm_campaign=Badge_Grade)

This PostgreSQL client is intended to satisfy KDE Plasma users who have low-spec hardware (Yepo laptops, Raspberry Pi etc.), those who already run Plasma or QT desktop and doesn't want fancy resources, which full database IDEs available like DBeaver already provides.

The goal is to keep a light, quick-starting, tiny usable interface with basic database features for software developers.

If you need complex database management features, have a decent modern workstation or if you don't use a Plasma/QT desktop, this is not the tool for you, there are plenty of other wonderful clients out there.

Bonus feature: funny dialogs for user interaction.

## Install steps:

This step is rather complicated, but I'm counting on you!

`
   $ pip install kquery
`

And then, to run:

`
   $ kquery
`

And that's it! 

## FAQ:
Q - Why did you choose PyQt5, a 100+MB framework for a "light" database client? You must be stupid to load that much dependency for such a small application.

A - Because this amount of space isn't a problem for me. Hard Disk space is plentiful and cheap nowadays, not as much as battery/memmory/processing in low-powered devices.

Q - Do you plan to provide other database connectors? Or improved PostgreSQL connecion features?

A - Yes! If I have enough time and application load time and performance is not compromised, why not?
