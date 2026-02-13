    let equalPressed = 0;
    const input = document.getElementById("input");
    const equal = document.getElementById("equal");
    const buttonInput = document.querySelectorAll(".button");
    const historialContent = document.getElementById("historialContent");

    // --- FUNCIONES MATEMÁTICAS ---
    const sinDeg = (x) => Math.sin(x * Math.PI / 180);
    const cosDeg = (x) => Math.cos(x * Math.PI / 180);
    const tanDeg = (x) => Math.tan(x * Math.PI / 180);
    const log = (x) => Math.log10(x);
    const ln = (x) => Math.log(x);
    const factorial = (n) => {
        if (n < 0) return NaN;
        if (n === 0) return 1;
        let res = 1;
        for (let i = 2; i <= n; i++) res *= i;
        return res;
    };

    // --- LOGICA DE CLIC EN BOTONES ---
    buttonInput.forEach((btn) => {
        btn.addEventListener("click", () => {
            if (equalPressed === 1) {
                input.value = "";
                equalPressed = 0;
            }

            const value = btn.getAttribute("data-number");

            if (value === "AC") {
                input.value = "";
            } else if (value === "DEL") {
                input.value = input.value.slice(0, -1);
            } else if (value) {
                input.value += value;
            }
        });
    });

    // --- BOTÓN IGUAL ---
    equal.addEventListener("click", () => {
        let exp = input.value;
        if (!exp) return;

        try {
            let formula = exp
                .replace(/\^/g, "**")
                .replace(/sin\(/g, "sinDeg(")
                .replace(/cos\(/g, "cosDeg(")
                .replace(/tan\(/g, "tanDeg(")
                .replace(/log\(/g, "log(")
                .replace(/ln\(/g, "ln(")
                .replace(/√\(/g, "Math.sqrt(")
                .replace(/(\d+)!/g, "factorial($1)");

            // Cerrar paréntesis automáticamente
            let openP = (formula.match(/\(/g) || []).length;
            let closeP = (formula.match(/\)/g) || []).length;
            while (openP > closeP) { formula += ")"; openP--; }

            let result = new Function(`return ${formula}`)();
            
            input.value = Number.isInteger(result) ? result : parseFloat(result.toFixed(4));
            equalPressed = 1;
            
            // Historial simple
            const item = document.createElement("div");
            item.innerHTML = `<small>${exp} = ${input.value}</small>`;
            historialContent.prepend(item);

        } catch (e) {
            alert("Error en la expresión");
            input.value = "";
        }
    });
