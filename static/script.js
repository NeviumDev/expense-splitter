document.addEventListener("DOMContentLoaded", () => {
    const forms = document.querySelectorAll("form");
    
    forms.forEach(form => {
      form.addEventListener("submit", () => {
        const toast = document.createElement("div");
        toast.className = "toast-message";
        toast.textContent = "✅ Datos guardados correctamente";
        document.body.appendChild(toast);
        setTimeout(() => toast.remove(), 2500);
      });
    });
  });
  
  // Estilo dinámico para el toast
  const style = document.createElement("style");
  style.innerHTML = `
  .toast-message {
    position: fixed;
    bottom: 30px;
    right: 30px;
    background: #198754;
    color: white;
    padding: 10px 18px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    opacity: 0;
    animation: fadeInOut 2.5s forwards;
    font-weight: 500;
  }
  @keyframes fadeInOut {
    0% { opacity: 0; transform: translateY(10px); }
    10%, 90% { opacity: 1; transform: translateY(0); }
    100% { opacity: 0; transform: translateY(10px); }
  }
  `;
  document.head.appendChild(style);
  