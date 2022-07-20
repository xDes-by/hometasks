function alerted(id){
    // alert("Вы нажали на кнопку " + id);
    const property = document.getElementById(id);
    property.style.backgroundColor = "#" + Math.floor(Math.random()*16777215).toString(16);
  }

const alerted2 = (id) => {
    const property = document.getElementById(id);
    const clientWidth = document.getElementById(id).clientWidth;
    const scale = clientWidth + 50
    property.style.width = scale + "px";
} 

const alerted3 = (id) => {
    alert("Че жмешь?")
} 