function findOutlier(integers){
    let mostlyEven;
    let outlier;

    if (integers[0] % 2 === 0) { // 0 is even
        if (integers[1] % 2 === 0) { // 0 and 1 are even so it's an even array
            mostlyEven = true;
        } else {                            // If first is even and second is odd, we need to check third
            if (integers[2] % 2 === 0) {   // If third is even, it's an even arrat
                mostlyEven = true;
            } else {                    // Else if third is odd, it's an odd array
                mostlyEven = false;
            }
        }
    } else {
        if (integers[1] % 2 !== 0) {  // If first and second are odd, then it's an odd array
            mostlyEven = false;
        } else {                        //If first is odd and second is even, we need to check third
            if (integers[2] % 2 === 0) {
                mostlyEven = true;
            } else {
                mostlyEven = false;
            }
        }
    }
    let i=0;
    let index;
    if (mostlyEven) {
        while (integers[i] % 2 === 0) {
            i++;
        }
        index = i;
    } else {
        while (integers[i] % 2 !== 0) {
            i++;
        }
        index = i;
    }
    outlier = integers[i];
    return outlier;
  }

 console.log(findOutlier([160, 3, 1719, 19, 11, 13, -21]));