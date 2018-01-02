function getContacts() {
  return fetch('http://localhost:5000/api/contacts')
    .then(data => data.json())
    .catch(console.log);
}

function createContact(contact) {
  return fetch('api/contacts', {
      method: 'POST',
      credentials: 'include',
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(contact)
    }).then(data => data.json)
      .catch(console.log)
}


export {getContacts, createContact}