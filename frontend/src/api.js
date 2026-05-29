import axios from "axios";

const API = axios.create({
    baseURL: "https://ai-support-agent-ogr-production.up.railway.app"
});

export default API;