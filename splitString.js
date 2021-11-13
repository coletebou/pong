function toCamelCase(str) {
  let wordsArr = str.split(/-|_/); //Splits string at dashes or underscores

  let capitalWordsArr = wordsArr.map((word) => {
    if (str.search(/^[A-Z]/) === -1 && wordsArr.indexOf(word) === 0) { // Don't change very first letter 
      return word;
    }
    return word[0].toUpperCase() + word.slice(1); //Capitalize first letter of each word
  });

  let camelString = capitalWordsArr.join(""); //Join the words back together with no space

  console.log(`Original String: ${str}`);
  console.log(`Capital Words Array: ${capitalWordsArr}`);
  console.log(`Camel String: ${camelString}`);
}

toCamelCase("hello-world-of-love");
