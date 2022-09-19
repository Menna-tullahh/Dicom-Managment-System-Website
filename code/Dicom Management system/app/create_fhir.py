import asyncio
from fhirpy import AsyncFHIRClient
from fhirpy.base.exceptions import ResourceNotFound, MultipleResourcesFound
import matplotlib.pyplot as plt

import dicom


async def save_fhir(mod_code, patientNationalID, seriesNo, instanceNo, uid, description, imgID):

    # Create an instance
    client = AsyncFHIRClient(
        'https://fhir.simplifier.net/BMD303-HL7',
        authorization='Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoibWVubmFhYmRlbHNhdHRhcjEiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjUxNTY5N2I3LTE0NTgtNGM2Mi04NGY5LTcwNDUzYTY1N2I1YSIsImp0aSI6IjAwMzM0NjcxLWQ1OTYtNGFhMS05NTBjLThjYjAwOWRlMTFhOCIsImV4cCI6MTYyNTkzMjExOSwiaXNzIjoiYXBpLnNpbXBsaWZpZXIubmV0IiwiYXVkIjoiYXBpLnNpbXBsaWZpZXIubmV0In0.IPtFQ1Wwoj_-BCiiHR97cQZR7iyq8EkYEsGdNJ5Muvw',
    )

    organization = client.resource(
        'ImagingStudy',
        id= imgID,
        description= imgID,
        # identifier={
        #     "value": imgID
        # },
        modality={
            "code": str(mod_code)
        },
        subject= {
            "reference": patientNationalID
        },
        numberOfSeries= seriesNo,
        numberOfInstances = instanceNo,
        #started = starttime,
        series={
            "uid" : uid,
            "description" : description
        },
    )
    await organization.save()

async def get_fhir(ID):
    # Create an instance
    client = AsyncFHIRClient(
        'https://fhir.simplifier.net/BMD303-HL7',
        authorization='Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoibWVubmFhYmRlbHNhdHRhcjEiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjUxNTY5N2I3LTE0NTgtNGM2Mi04NGY5LTcwNDUzYTY1N2I1YSIsImp0aSI6IjAwMzM0NjcxLWQ1OTYtNGFhMS05NTBjLThjYjAwOWRlMTFhOCIsImV4cCI6MTYyNTkzMjExOSwiaXNzIjoiYXBpLnNpbXBsaWZpZXIubmV0IiwiYXVkIjoiYXBpLnNpbXBsaWZpZXIubmV0In0.IPtFQ1Wwoj_-BCiiHR97cQZR7iyq8EkYEsGdNJ5Muvw',
    )
    res = client.resources('ImagingStudy')
    print(ID)

    x = await res.fetch()
    for item in x:
        if str(item.id) == str(ID):
            print("fsaljdfasfasf {}".format(item.id))
            return x[x.index(item)]


