import http from 'k6/http';
import { sleep } from 'k6';
import { URL } from 'https://jslib.k6.io/url/1.0.0/index.js';
export const options = {
  vus: 120,
  duration: '60s',
};
export default function () {
  const emails = ["victor.muchiaroni@brmalls.com.br", "teste@brmalls.com.br", "teste@hotmail.com", "teste@gmail.com"];
  const products = ["rice", "beans", "lettuce", "tomatoes"];
  const email_random = Math.floor(Math.random() * emails.length);
  const products_random = Math.floor(Math.random() * products.length);
  const payload = {
    'email': emails[email_random],
    'products': products[products_random]
  };
  const svc_url = 'https://api-dev.brmalls.com.br/brmalls-app-hydra/oauth2/auth';
  const test = svc_url + '/oauth2/auth';


  const params = {
    headers: {
        'Content-Type': 'application/json'
    },
  };

  let retry =  http.get(test);
  sleep(1);
}
