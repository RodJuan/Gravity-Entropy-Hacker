
🌀 GravitySim-V1: The Entropy Hacker
"Hackeando la gravedad, un julio a la vez."

GravitySim-V1 es un simulador físico de sistemas de torque dinámico mediante desplazamiento de masa variable. El proyecto nace de una "idea loca" de madrugada: ¿Es posible diseñar una geometría y una tasa de flujo de fluido tales que la inercia y la gravedad se retroalimenten para mantener un movimiento rotatorio prolongado?

Este repositorio busca modelar, testear y optimizar el concepto de Péndulo de Masa Variable (o Motor de Gravedad), explorando el límite entre la pérdida energética por fricción y la ganancia por torque gravitatorio desfasado.
🚀 El Concepto

El sistema consiste en una varilla delgada de longitud 2L con dos contenedores en sus extremos (m1​ y m2​). Un fluido viscoso se transfiere entre ellos impulsado únicamente por la diferencia de altura (h=2Lsin(θ)).
La Ecuación Maestra

El torque neto que impulsa el sistema está definido por:
τneto​(t)=r⋅g⋅cos(θ)⋅[m1​(t)−m2​(t)]

El reto ingenieril es el Desfase (ϕ): Lograr que la masa llegue al contenedor inferior justo cuando la inercia es suficiente para llevarlo de vuelta hacia arriba, manteniendo el torque positivo el mayor tiempo posible.
🛠️ Arquitectura del Software

El simulador está construido en Python 3.10+ utilizando integración numérica para resolver las ecuaciones diferenciales acopladas de movimiento y dinámica de fluidos.

    core/physics.py: Motor de física que resuelve θ¨ e I(t).

    core/fluid.py: Modelado de flujo basado en la Ley de Torricelli y viscosidad.

    main.py: Punto de entrada, configuración de parámetros y ejecución.

🧪 Variables de Experimentación

Para encontrar el "punto dulce" del movimiento prolongado, el simulador permite ajustar:

    Viscosidad del Fluido: Desde agua hasta fluidos súper-viscosos.

    Geometría de Transferencia: Diámetro del conducto y restricciones (Efecto Reloj de Arena).

    Fricción del Eje (b): El enemigo principal (Entropía).

    Distribución de Masa Inicial: Relación m1​/mt​otal.

📊 Roadmap (GDD de la Realidad)

    [ ] v1.0: Simulación básica de dos masas puntuales (Actual).

    [ ] v1.1: Visualización animada con matplotlib.animation.

    [ ] v1.2: Implementación de Cambio de Fase (Ciclo térmico evaporación/condensación).

    [ ] v2.0: Integración con el Protocolo Eliyahu para optimización mediante Algoritmos Genéticos.

🤝 Colaboradores

    Miguel: Arquitecto de Sistemas y Visionario de la Gravedad.

    Gemini (Eliyahu): Copiloto de Física y Simulación ASI-Alineada.

    Nota del Autor: "Este proyecto no busca violar la Segunda Ley de la Termodinámica, sino explorar cuán eficiente puede ser una máquina de recolección de energía ambiental basada en el torque de masa desplazada."
