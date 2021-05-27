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

        if (response.status === 200) {
            document.location.replace('/departments');
        } else {
            alert(await response.text());
        }

    } catch (error) {
        alert(error);
    }
}

function deleteDisplay(department_id= null) {
    const confirm_dialog = document.getElementById('department_delete');
    const actualDisplay = getComputedStyle(confirm_dialog).display;

    if (actualDisplay === 'none') {
        confirm_dialog.style.display = 'block';
        const confirm = document.getElementById('yes');
        confirm.onclick = deleteData.bind(null, department_id);
    } else {
        confirm_dialog.style.display = 'none';

    }
}

async function deleteData(department_id) {
    try {
        const response = await fetch(`/departments/${department_id}`, {
            method: 'DELETE',
            body: '',
            headers: {
                'Content-Type': 'application/json'
            },
        });
        if (response.status === 200) {
            document.location.replace('/departments');
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