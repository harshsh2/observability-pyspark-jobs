import { ConfigCompiler } from "ondc-code-generator";
import { SupportedLanguages } from "ondc-code-generator/dist/types/compiler-types";
import path from "path";
import { readFileSync } from "fs";
import { loadAndDereferenceYaml } from "./utils/yaml-utils.js";

const runCompiler = async (buildYaml: any, outputPath: string) => {
  const comp = new ConfigCompiler(SupportedLanguages.Python);
  const buildString = buildYaml;
  const buildParsed = (await loadAndDereferenceYaml(buildString)) as any;
  const valParsed = buildParsed["x-validations"];
  await comp.initialize(buildString);
  //   const x_validations = JSON.parse(valParsed) as any;
  await comp.generateCode(
    valParsed as any,
    "l1_validations",
    false,
    outputPath
  ); // pass the validations object and the name of the function of the generated code
};

let domain = "RET10";
const buildYaml = readFileSync(
  path.join(process.cwd(), `./build-yaml/${domain}/build.yaml`),
  "utf8"
);
const outputPath = path.join(process.cwd(), `../validations/${domain}/`);
runCompiler(buildYaml, outputPath);
