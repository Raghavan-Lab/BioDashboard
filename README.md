# BioDashboard
###### A flask based web took kit for biology research.
---
The BioDashboard project will contain small and useful biology research tools that cab be hosted on local lab computers.  An example of a useful tool would be a 'Find Orthologs' tool that uses a reciprocal best blast hit to identify punitive orthologs.  It will accept two genbank, or amino acid files and perform a reciprocal best blast hit between them.  The resulting ortholog list will be displayed back to the user.  Later versions will allow for storage of these ortholog lists using a SQLite3 database.


#### Adding Tools
---
New tools will show up in the main table of contents when they are added to the config.py file in the TOOLS variable.  Additionally their custom views will need to be added to the import statement located in the app/\_\_init\_\_.py file.

