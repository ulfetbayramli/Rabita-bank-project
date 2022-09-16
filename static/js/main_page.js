/* Calculator */
/* Inputs */
const calcInp1 = document.getElementById("calcInp1");
const calcInp2 = document.getElementById("calcInp2");
const calcInp3 = document.getElementById("calcInp3");
const calcRange1 = document.getElementById("calcRange1");
const calcRange2 = document.getElementById("calcRange2");
const calcRange3 = document.getElementById("calcRange3");

/* Results */
const resultAll = document.querySelector(".resultAll");
const resultPersentage = document.querySelector(".resultPersentage");
const resultMonthsly = document.querySelector(".resultMonthsly");

calcRange1.value = 3;
calcRange1.addEventListener("input", () => {
  calcInp1.value = calcRange1.value;
  calc();
});

calcInp1.addEventListener("input", () => {
  calcRange1.value = calcInp1.value;
  calcInp1.value > 36 && (calcInp1.value = 36);
  calc();
});

calcRange2.value = 10150;
calcRange2.addEventListener("input", () => {
  calcInp2.value = calcRange2.value;
  calc();
});

calcInp2.addEventListener("input", () => {
  calcRange2.value = calcInp2.value;
  calcInp2.value > 20000 && (calcInp2.value = 20000);
  calc();
});

calcRange3.value = 12;
calcRange3.addEventListener("input", () => {
  calcInp3.value = calcRange3.value;
  calc();
});

calcInp3.addEventListener("input", () => {
  calcRange3.value = calcInp3.value;
  calcInp3.value > 30 && (calcInp3.value = 30);
  calc();
});

const calc = () => {
  resultAll.innerHTML = calcInp1.value + ".00 AZN";
  resultPersentage.innerHTML = calcInp2.value + ".00 AZN";
  resultMonthsly.innerHTML = calcInp3.value + ".00 AZN";
};

calc();
