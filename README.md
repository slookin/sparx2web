# sparx2web
automatization tool, allow to export full SparxEA model to set of HTML files.

## configuration
### config.yaml

- repository: link to repository (file path, cloud link or ODBC link)
- login: user login
- password: user password
- models: - list of dict
 - - model: name of model in repository
 - - path: path for export
                       
### Compatibilty
It was tested with Sparx EA 13.0, Sparx EA 13.5.

Sparx EA 13.5 has a small problem with authentication in repositories.
