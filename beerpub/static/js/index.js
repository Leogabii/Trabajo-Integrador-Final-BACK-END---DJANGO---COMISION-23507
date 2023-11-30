
// USO DE MI FW

import { Render } from "./Render.js";
import { veronicaSuperPower } from "./VeronicaSuperPower.js";
import { convertir } from "./convertir.js";






const app = new Render("app");

const JSON_LOCALBEER = "./js/imagen.json";
const JSON_LOCAL = "./js/beer.json";
const JSON_LOCALS = "./js/beers.json";
const API_URI = "https://api.sampleapis.com/beers/stouts";
const API_BEERPUB = "http://127.0.0.1:5000/beerpub/beerpub/";
const API_breakpoint="http://127.0.0.1:5000/beerpub/";
const API_acceso="http://127.0.0.1:5000/api/";
const API_pruebaMil = "http://127.0.0.1:8000/api/";

app.fetchData(API_pruebaMil , veronicaSuperPower,convertir);
