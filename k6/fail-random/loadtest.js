import http from 'k6/http';
import { sleep } from 'k6';
import { URL } from 'https://jslib.k6.io/url/1.0.0/index.js';
export const options = {
  vus: 20,
  duration: '60',
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
  const svc_url = 'http://client-api.client-api.svc.cluster.local:8000';
  const url_create = svc_url + '/create/cart';
  const url_get = new URL(svc_url + '/get/carts');
  const url_retry = svc_url + '/retries/upstream/cart/1'
  url_get.searchParams.append('email', emails[email_random]);

  const params = {
    headers: {
        'Content-Type': 'application/json'
    },
  };

  let create_cart = http.post(url_create, JSON.stringify(payload),params);
  let get_cart =  http.get(url_get.toString());
  let retry =  http.get(url_retry);
  sleep(1);
}
