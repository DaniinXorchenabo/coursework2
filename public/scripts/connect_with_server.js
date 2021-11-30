const button_handler = (event) => {
    console.log(event.target.id)
    setTimeout(() => {
        const xhr = new XMLHttpRequest();
        const start = document.getElementById(`${event.target.id}_from`).value;
        const end = document.getElementById(`${event.target.id}_to`).value;
        const setup_count = 10;
        xhr.open(
            'GET',
            `${document.location.protocol}//${document.location.host}/get_graphs_data?array_type=${event.target.id}&start=${start}&end=${end}&setup_count=${setup_count}`,
            true);

        xhr.send();
        xhr.onreadystatechange = () => { // (3)
            if (xhr.readyState !== 4) return;

            // button.innerHTML = 'Готово!';

            if (xhr.status !== 200) {
                console.log(xhr.status + ': ' + xhr.statusText);
            } else {
                console.log(xhr.responseText);
            draw_graph( JSON.parse( xhr.responseText));
            }

        }

    });
}


[...document.querySelectorAll('button')].map(
    el => el.addEventListener('click', button_handler, {once: false}))
