# **Cards Game**

Un jeu de carte classique sur terminal

## Aperçu

![preview](preview.gif)

### Consignes

La liste des consignes du sujet est disponible dans le [TODO.md](TODO.md)

## Pré-requis

L'installation de [**Python 3**](https://www.python.org/downloads/) est recommandé pour l'éxécution du script

## Dépendances

- [json](https://docs.python.org/3/library/json.html)
- [os.system](https://docs.python.org/3/library/os.html#os.system)
- [platform.system](https://docs.python.org/3/library/platform.html#platform.system)
- [random.shuffle](https://docs.python.org/3/library/random.html#random.shuffle)
- [sys.argv](https://docs.python.org/3/library/sys.html#sys.argv)
- [time.sleep](https://docs.python.org/3/library/time.html#time.sleep)

## Utilisations

Exécution du script: `$ python main.py <arg>`

| Arguments                        | Valeur                  | Descriptions                                |
| -------------------------------- | ----------------------- | ------------------------------------------- |
| `-s <x>`, `--show-card <x>`      | `<x>` n° de carte       | Affiche une carte du paquet                 |
| `-S`, `--show-all`               | -                       | Affiche tout le paquet de cartes            |
| `-r <x>`, `--show-rand-card <x>` | `<x>` n° de carte       | Affiche une carte du paquet mélangé         |
| `-R`, `--show-rand-all`          | -                       | Affiche toutes les cartes du paquet mélangé |
| `-g`, `--game`                   | `<gameName>` nom du jeu | Lance un jeu de carte                       |
| `-h`, `--help`                   | -                       | Affiche le menu d'aide                      |
| `-d`, `--debug`                  | -                       | Exécution en mode debuger                   |
| `-v`, `--version`                | -                       | Affiche la version du programme             |

## Options & Configurations

La configuration du programme se fait depuis le fichier [`config.json`](config.json) au format **JSON**, dans ce fichier vous pouvez **configurer la langue**.

La langue par défaut du programme est **l'anglais**.

```json
{
  "lang": "fr"
}
```

## Ressource disponibles

### Langues & Régions

Les langues disponibles sont contenus dans le fichier [`regions.json`](core/regions.json) disponible dans le dossier [`core/`](core/). Il contient les traductions **françaises** et **anglaises** du programme, vous pouvez en ajouter d'autre si vous le souhaitez, vous n'aurez alors qu'à spécifier son label (`"fr"`) avec tous son contenus.

### Jeux implémenter

| Nom du jeu                                                                          | Jouable |
| ----------------------------------------------------------------------------------- | ------- |
| [La Bataille Fermée](<https://fr.wikipedia.org/wiki/Bataille_(jeu)>)                | Oui     |
| [Le Solitaire](<https://en.wikipedia.org/wiki/Klondike_(solitaire)>)                | Non     |
| [La Dame de Pique](<https://fr.wikipedia.org/wiki/Dame_de_pique_(jeu)>)             | Non     |
| [Le Pouilleux (Mistigri)](https://fr.wikipedia.org/wiki/Pouilleux)                  | Non     |
| [Le Menteur](https://ludos.brussels/ludo-walalou/opac_css/doc_num.php?explnum_id=5) | Non     |

## Licence

Code sous license [GPL v3](LICENSE)
