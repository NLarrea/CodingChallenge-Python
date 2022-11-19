/*
Reto #45
CONTENEDOR DE AGUA
Fecha publicación enunciado: 07/10/22
Fecha publicación resolución: 14/11/22
Dificultad: MEDIA

Enunciado: Dado un array de números enteros positivos, donde cada uno representa unidades
de bloques apilados, debemos calcular cuantas unidades de agua quedarán atrapadas entre ellos.

- Ejemplo: Dado el array [4, 0, 3, 6, 1, 3].

       ⏹
       ⏹
  ⏹💧💧⏹
  ⏹💧⏹⏹💧⏹
  ⏹💧⏹⏹💧⏹
  ⏹💧⏹⏹⏹⏹

Representando bloque con ⏹︎ y agua con 💧, quedarán atrapadas 7 unidades de agua.
Suponemos que existe un suelo impermeable en la parte inferior que retiene el agua.

Statement: Given an array of positive integers, where each represents units of stacked blocks, we must calculate how many units of water will be trapped between them.
of stacked blocks, we must calculate how many units of water will be trapped between them.

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

function calculateWaterUnits(blockList){
    // if there is a negative number -> return message
    if(blockList.some(num => num < 0)) return "All numbers must be positive!";
    // variables
    let waterUnits = 0; // this will be the result
    let wall = 0;
    let nextWall = 0;
    blockList.forEach((block, index) => {
        if(index !== blockList.length-1 && (index === 0 || nextWall === block)){
            wall = (index === 0)? block : nextWall;
            nextWall = 0;
            // calculate nextWall
            for(let nextBlockIndex = index+1; nextBlockIndex<blockList.length; nextBlockIndex++){
                if(blockList[nextBlockIndex] >= nextWall) nextWall = blockList[nextBlockIndex];
            }
        } else {
            // calculate waterUnits
            let referenceWall = (nextWall > wall)? wall : nextWall;
            let currentBlocks = referenceWall - block;
            waterUnits += (currentBlocks >= 0)? currentBlocks : 0;
        }
    })
    return waterUnits; // return the solution
}

console.log(calculateWaterUnits([4, 0, 3, 6])); // 5
console.log(calculateWaterUnits([4, 0, 3, 6, 1, 3])); // 7
console.log(calculateWaterUnits([5, 4, 3, 2, 1, 0])); // 0
console.log(calculateWaterUnits([0, 1, 2, 3, 4, 5])); // 0
console.log(calculateWaterUnits([4, 0, 3, 6, 1, 3, 0, 1, 6])); // 24