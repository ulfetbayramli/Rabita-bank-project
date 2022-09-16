/* Showing Search Input Part */
const svg = document.querySelector(".searchShow");
const search_container = document.querySelector(".search_container");
const search_input = document.querySelector(".search_input");

const showSearch = () => {
  search_container.classList.add("search_container_active");
  search_input.classList.add("search_container_active");
};

const closeSearch = () => {
  search_container.classList.remove("search_container_active");
  search_input.classList.remove("search_container_active");
};

const stopPropagation = (e) => {
  e.stopPropagation();
};

svg.addEventListener("click", showSearch);
window.addEventListener("click", closeSearch);

/* Currency calculator */
const select1 = document.querySelector(".select1");
const select2 = document.querySelector(".select2");
const currency_input = document.querySelector(".currency_input");
const currency_result = document.querySelector(".currency_result");
let k = 2;

const ui = () => {
  currency_result.innerHTML = (currency_input.value * k).toFixed(2);
};

var myHeaders = new Headers();
myHeaders.append("apikey", "ifngs2e7SCPc4Pb45K2fa5alERIZsLn5");

var requestOptions = {
  method: "GET",
  redirect: "follow",
  headers: myHeaders,
};

const fetchingData = async () => {
  let first = select1.value;
  let second = select2.value;
  let response = await fetch(
    `https://api.apilayer.com/fixer/convert?to=${second}&from=${first}&amount=1`,
    requestOptions
  );
  let res = await response.json();
  k = res?.info?.rate;
  ui();
};

select1.addEventListener("change", fetchingData);
select2.addEventListener("change", fetchingData);
currency_input.addEventListener("input", ui);
fetchingData();
