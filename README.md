# Nomad SiC Defects Database
 <img src="docs/assets/nomad_plugin_logo.png" alt="Nomad Plugin" width="200">

## Introduction

Welcome to the NOMAD plugin for the Silicon Carbide (SiC) Defects Database. This plugin defines a structured data model for experimentally observed defects in SiC, enabling consistent storage, search, and reuse within NOMAD. In future, the data can hopefully be accessed via the NOMAD API and explored in the 'SiC Defect Search App'. 

 <img src="docs/assets/ScreenshotSicDefectApp.png" alt="SiC Defect App" width="600">

## Overview

This plugin provides a schema for representing defects in SiC materials.
It enables:

- standardized representation of defect data
- integration into NOMAD archives
- earch and comparison of experimentally observed defects

Each database entry corresponds to a single experimentally observed defect reported in the literature. 

## Data Model

The schema defines:

- Defect description: properties and characteristics of the defect
- Host material: currently limited to Silicon Carbide (SiC)
- Literature references: links to the original publication(s)
- Structured metadata: enabling search and filtering in NOMAD

## Adding this plugin to NOMAD

Currently, NOMAD has two distinct flavors that are relevant depending on your role as an user:
1. [A NOMAD Oasis](#adding-this-plugin-in-your-nomad-oasis): any user with a NOMAD Oasis instance.
2. [Local NOMAD installation and the source code of NOMAD](#adding-this-plugin-in-your-local-nomad-installation-and-the-source-code-of-nomad): internal developers.

### Adding this plugin in your NOMAD Oasis

Read the [NOMAD plugin documentation](https://nomad-lab.eu/prod/v1/staging/docs/howto/oasis/plugins_install.html) for all details on how to deploy the plugin on your NOMAD instance.

### Adding this plugin in your local NOMAD installation and the source code of NOMAD

We now recommend using the dedicated [`nomad-distro-dev`](https://github.com/FAIRmat-NFDI/nomad-distro-dev) repository to simplify the process. Please refer to that repository for detailed instructions.


## Main contributors
| Name | E-mail     |
|------|------------|
| Nina Hälterlein | [nina.haelterlein@fau.de](mailto:nina.haelterlein@fau.de)
