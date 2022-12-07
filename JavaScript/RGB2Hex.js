function rgb(r, g, b) {
  let rgbArray = [r, g, b];
  let hexArray = [
    [0, 0], //red
    [0, 0], //green
    [0, 0], //blue
  ];
  let hexString = "#000000";

  //Check for Out-Of-Range Values
  for (let color of rgbArray) {
    if (color > 255) {
      rgbArray[rgbArray.indexOf(color)] = 255;
    } else if (color < 0) {
      rgbArray[rgbArray.indexOf(color)] = 0;
    }
  }

  //Convert values to decimal pairs
  for (let i = 0; i < 3; i++) {
    hexArray[i][0] = Math.floor(rgbArray[i] / 16); // First digit in color
    hexArray[i][1] = rgbArray[i] - 16 * hexArray[i][0]; //Second digit in color
  }

  //convert decimal pairs to hex using unicode
  hexArray = hexArray.map((pair) => {
    let firstDigit = pair[0];
    let secondDigit = pair[1];
    if (firstDigit > 9) {
      firstDigit += 55;
      firstDigit = String.fromCharCode(firstDigit);
    }
    if (secondDigit > 9) {
      secondDigit += 55;
      secondDigit = String.fromCharCode(secondDigit);
    }
    return [firstDigit, secondDigit];
  });

  //Combine Pairs into one value
  for (let i = 0; i < 3; i++) {
    hexArray[i] = hexArray[i].join("");
  }
  //Join final 3 values into one string
  hexString = hexArray.join("");

  //Add octothorpe
  return `#${hexString}`;
}

console.log(rgb(255, 255, 255));
