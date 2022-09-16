/* Modal */
const share_modal = document.querySelector(".share_modal");
const share = document.querySelector(".share");
const close_btn = document.querySelector(".btn-close");

const showModal = () => {
  share_modal.classList.remove("d-none");
};

const closeModal = () => {
  share_modal.classList.add("d-none");
};

share.addEventListener("click", showModal);
close_btn.addEventListener("click", closeModal);

window.addEventListener("click", closeModal);
