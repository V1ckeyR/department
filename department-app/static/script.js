function putDepartment(department_id) {
    const inputs = document.getElementById('put').elements;
    const data = {
        'name': inputs['name'].value
    }

    fetch(`/departments/${department_id}`, {
            method: 'PUT',
            body: JSON.stringify(data),
            headers: {
              'Content-Type': 'application/json'
            },
        }).then(response => {
            if (response.ok) {
                window.location = document.referrer;
            } else {
                alert(response.text());
            }
        }).catch (e => alert(e))
}

function putEmployee(employee_id) {
    const form = document.querySelector('#put_employee');

    const data = ((form) => {
        let obj = {};
        const formData = new FormData(form);
        for (let key of formData.keys()) {
            obj[key] = formData.get(key);
        }
        return JSON.stringify(obj);
    })(form);

    fetch(`/employees/${employee_id}`, {
            method: 'PUT',
            body: data,
            headers: {
              'Content-Type': 'application/json'
            },
        }).then(response => {
            if (response.ok) {
                window.location = document.referrer;
            } else {
                alert(response.text());
            }
        }).catch (e => {
            alert(e)
    })
}

function deleteDisplay(id, url = null, toRefer = null) {
    const confirm_dialog = document.getElementById(id);
    const actualDisplay = getComputedStyle(confirm_dialog).display;

    if (actualDisplay === 'none') {
        confirm_dialog.style.display = 'block';
        const confirm = document.getElementById(`${id}_yes`);
        confirm.onclick = deleteData.bind(null, url, toRefer);
    } else {
        confirm_dialog.style.display = 'none';
    }
}

function deleteData(url, toRefer) {
    fetch(url, {
            method: 'DELETE',
            body: '',
            headers: {
                'Content-Type': 'application/json'
            },
        }).then(response => {
            if (response.ok) {
                if (toRefer) {
                    window.location = document.referrer
                } else {
                    window.location.reload();
                }

            } else {
                alert(response.text())
            }
        }).catch(e => alert(e))
}

function cancel() {
    window.history.back();
}