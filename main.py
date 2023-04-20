from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from contact import Contact
from contact_services import ContactSevices

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/contacts/")
async def read_all():

    result = ContactSevices.get_contact_postgres()

    response_final = [{
        "id": item[0],
        "name": item[1],
        "phone": item[2],
        "email": item[3]
    }for item in result
    ]

    return response_final


@app.get("/contacts/{id}")
async def read_one(id: int):

    result = ContactSevices.get_one_contacts_postgres(id)

    response_final = [{
        "id": item[0],
        "name": item[1],
        "phone": item[2],
        "email": item[3]
    }for item in result
    ]

    return response_final


@app.post("/contacts/")
def create_contact(contact: Contact):

    ContactSevices.post_contacts_postgres(contact)

    return {f"Sucess Created"}


@app.delete("/contacts/{id}")
def delete_contact(id: int):

    x = ContactSevices.delete_contact_postgres(id)
    return {f"Sucess : Deleted"}


@app.put("/contacts/{id}")
def update_contact(contact: Contact, id: int):

    x = ContactSevices.update_contact_postgres(
        contact, id)

    return {f"Sucess Updated"}
