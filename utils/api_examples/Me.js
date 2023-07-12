(async function() {
    console.clear();
    const headers = {
        Authorization: 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5MjAzMzExLCJpYXQiOjE2ODkxOTk3MTEsImp0aSI6IjVjMzY2NjQyMGZlOTQyZWU5YzAyMDI3NDk4OTc1ZWNiIiwidXNlcl9pZCI6OH0.vOud2vRZWONYXvWfPhLfvL4GNMZ0qcNpZgxE3edQSEQ'
    };
    const config = {
        method: 'GET',
        headers: headers
    };
    const response = await fetch(
        'http://127.0.0.1:8000/authors/api/me/',
        config
    );
    
    const json = await response.json();
    
    console.log('STATUS', response.status);
    console.log(json);
})();