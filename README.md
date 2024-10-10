## UPM package manager

### Features

- **Support For Multiple Programming Languages At Once**

UPM seamlessly handles package management for Programming languages like Python or JavaScript with no 
need to install any outside package managers like `pip` or `npm`, thus , making it a versatile tool for developers
working in different environments

- **Downloading Files In A Compressed Format**

UPM downloads files in a compressed format like `.whl` (wheel) or `.tgz` (tarball) reducing bandwidth usage, speeding
up the package delivery process and prioritizing and saving space on the disk 

- **On-Demand Extraction Or Initializing**

Once a package is installed, you can choose when to extract or initialize the contents, giving you more control 
over the deployment process, and and, as mentioned above saving and prioritizing space on the disk

### how to use

- **To install a package**
- * ` UPM --py --install <package-name> `
- * ` UPM --js --install <package-name> `

- **To decompress a package**
- * ` UPM --py --decompress <package-name> `
- * ` UPM --js --decompress <package-name> `

### Supported Languages ( so far )
* JavaScript
* Python

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

> [!NOTE]
> There is no automatic adding to PATH support yet
