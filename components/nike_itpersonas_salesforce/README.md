
# NikeITPersonasSalesforce

This Yeager Component takes a NikeITPersonasInput model with a list of URLs or APIs that contain the information about Nike employees in the IT department as input. It then processes the input and saves the names and emails of the employees into the Salesforce API. After saving the data, it returns a NikeITPersonasOutput model containing a list of dictionaries with the names and emails of Nike employees in the IT department and the response from the Salesforce API.

## Initial generation prompt
description: "IOs - input:\n  class: NikeITPersonasInput\n  description: A NikeITPersonasInput\
  \ model with a list of URLs or APIs that contain\n    the information about Nike\
  \ employees in the IT department.\noutput:\n  class: NikeITPersonasOutput\n  description:\
  \ A NikeITPersonasOutput model containing a list of dictionaries with\n    the names\
  \ and emails of Nike employees in the IT department and the response from\n    the\
  \ Salesforce API after saving the information.\n"
name: NikeITPersonasSalesforce


## Transformer breakdown
- 1. Extract the list of URLs or APIs from the NikeITPersonasInput object.
- 2. Call each URL or API to collect the data of Nike employees.
- 3. Extract the names and emails of the employees.
- 4. Save the data into Salesforce API.
- 5. Get the response from Salesforce API after saving the data.
- 6. Create a NikeITPersonasOutput object with the list of dictionaries containing the names, emails and Salesforce response.
- 7. Return the NikeITPersonasOutput object.

## Parameters
[]

        