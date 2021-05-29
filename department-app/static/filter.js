window.onload = () => {
    document.querySelector("#start")
            .addEventListener('change', (event) => {
                const finish = document.querySelector('#finish').valueOf()
                filter(event.target.valueOf().value, finish.value)
            });

    document.querySelector('#finish')
            .addEventListener('change', (event) => {
                const start = document.querySelector('#start').valueOf()
                filter(start.value, event.target.valueOf().value)
            });
}

filter = (start, finish) => window.location = `/employees?start=${start}&finish=${finish}`