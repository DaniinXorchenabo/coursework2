const button_handler = (event) => {
    console.log(event.target.id);
    setTimeout(() => {
        const xhr = new XMLHttpRequest();
        const start = document.getElementById(`${event.target.id}_from`).value;
        const end = document.getElementById(`${event.target.id}_to`).value;
        const setup_count = document.getElementById("iteration_count").value;
        const graph_text = event.target.attributes.graph_text.nodeValue;
        console.log(event, graph_text)

        let alert_text = '';

        console.log(Number.isInteger(Number(start) ), start, (Number(start) % 1).toString() ,  start, (Number(start) % 1).toString() === start, (Number(setup_count) % 1).toString(), setup_count, (Number(setup_count)).toString() === setup_count)

        if ((Number(start)).toString() === start){
            if (Number(start) >= 0) {

            } else {
                alert_text += 'Поле  "От" должно быть целым не отрицательным числом\n'
            }

        } else {
            alert_text += 'Поле "От" должно являться целым не отрицательным целым числом\n'
        }
        if ((Number(setup_count)).toString() === setup_count){
            if (Number(setup_count) > 0) {

            } else {
                alert_text += 'Поле  "Количество итераций" должно быть целым не отрицательным числом\n'
            }

        } else {
            alert_text += 'Поле "Количество итераций" должно являться целым не отрицательным числом\n'
        }
        if ((Number(end)).toString() === end){
            if (Number(end) > 0) {
                if ((Number(start)).toString() === start && (Number(end)).toString() === end && Number(start) < Number(end)){

                } else {
                    alert_text += 'Поле  "До" должно быть целым не отрицательным числом, большим чем поле "От"\n'
                }
                if ((Number(end)).toString() === end && (Number(setup_count)).toString() === setup_count && Number(setup_count) <= Number(end)){

                } else {
                    alert_text += 'Поле  "До" должно быть целым не отрицательным числом, большим чем поле "количество итераций"\n'
                }
            } else {
                alert_text += 'Поле  "До" должно быть целым не отрицательным числом, большим чем поле "От"\n'
            }

        } else {
            alert_text += 'Поле "До" должно являться целым не отрицательным целым числом, большим чем поле "От"\n'
        }


        if (alert_text === '') {
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
                    draw_graph(JSON.parse(xhr.responseText), graph_text);
                }

            }
        } else {
            alert(alert_text);
        }
    });

}


[...document.querySelectorAll('button')].map(
    el => el.addEventListener('click', button_handler, {once: false}))
