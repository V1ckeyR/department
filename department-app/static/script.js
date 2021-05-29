async function put(department_id) {
    const inputs = document.getElementById('put').elements;
    const data = {
        'name': inputs['name'].value
    }

    try {
        const response = await fetch(`/departments/${department_id}`, {
            method: 'PUT',
            body: JSON.stringify(data),
            headers: {
              'Content-Type': 'application/json'
            },
        });

        if (response.ok) {
            document.location.replace('/departments');
        } else {
            alert(await response.text());
        }

    } catch (error) {
        alert(error);
    }
}

function deleteDisplay(page, id= null) {
    const confirm_dialog = document.getElementById(`${page}_delete`);
    const actualDisplay = getComputedStyle(confirm_dialog).display;

    if (actualDisplay === 'none') {
        confirm_dialog.style.display = 'block';
        const confirm = document.getElementById('yes');
        confirm.onclick = deleteData.bind(null, page, id);
    } else {
        confirm_dialog.style.display = 'none';

    }
}

async function deleteData(page, id) {
    try {
        const response = await fetch(`/${page}/${id}`, {
            method: 'DELETE',
            body: '',
            headers: {
                'Content-Type': 'application/json'
            },
        });
        if (response.ok) {
            document.location.replace(`/${page}`);
        } else {
            alert(await response.text());
        }
    } catch (e) {
        alert(e);
    }
}

function cancel() {
    window.history.back();
}