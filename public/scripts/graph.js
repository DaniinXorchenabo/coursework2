// const rand = () => Math.random();
// const new_data = (trace) => Object.assign(trace, {y: x.map(rand)});
//
// // add random data to three line traces
// let data = [
//     {mode: 'lines', line: {color: "#b55400"}},
//     {mode: 'lines', line: {color: "#393e46"}},
//     {mode: 'lines', line: {color: "#222831"}}
// ].map(new_data);
// console.log(data)
const layout = {
    title: 'Типы сортировок',
    uirevision: 'true',
    xaxis: {autorange: true},
    yaxis: {autorange: true}
};

Plotly.react('my_graph', [], layout);

const myPlot = document.getElementById('my_graph');

let cnt = 0;

const updating_graph_data = ([key, value, default_obj], index) => {
    // console.log(key, value, default_obj, index)
    return Object.assign(default_obj, {
        x: [...Object.keys(value)],
        y: [...Object.values(value)],
         name: key
    })
}

const draw_graph = (sorts_data, graph_text="Типы сортировок") => {

    let graph_data = [
        {mode: 'lines', line: {color: "#b55400"}},
        {mode: 'lines', line: {color: "#005cfa"}},
        {mode: 'lines', line: {color: "#27c400"}}
    ]
    // console.log([...Object.entries(sorts_data)])
    let local_data = [...Object.entries(sorts_data)]
        .map((el, ind) => el.concat([graph_data[ind]]))
        .map(i => {console.log(i); return i})
        .map(updating_graph_data);
    layout.title = graph_text;
    console.log( layout.title)
    layout.xaxis.autorange = true;
    layout.yaxis.autorange = true;

    // not changing uirevision will ensure that user interactions are unchanged
    // layout.uirevision = rand();

    Plotly.react('my_graph', local_data, layout);
}


// const interval = setInterval(() => {
//     data = data.map(new_data);
//
//     // user interaction will mutate layout and set autorange to false
//     // so we need to reset it to true
//     layout.xaxis.autorange = true;
//     layout.yaxis.autorange = true;
//
//     // not changing uirevision will ensure that user interactions are unchanged
//     // layout.uirevision = rand();
//
//     Plotly.react('my_graph', data, layout);
//     if (cnt === 100) clearInterval(interval);
// }, 2500);