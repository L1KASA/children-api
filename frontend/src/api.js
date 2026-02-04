import './config'
import axios from 'axios'

export async function GetClients() {
    const url = `${global.config.host}/children/?status=client`
    return axios.get(url).then(response => {
        return response.data.children
    }).catch(error => {
        return null
    })
}