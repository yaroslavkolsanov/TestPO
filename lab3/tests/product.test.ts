import { test, expect } from '@playwright/test';

test('API should return list of products', async ({ page }) => {
  await page.goto('http://localhost:8080/');
  await page.waitForSelector('.gallery__item.card', { timeout: 5000 });
  const productList = page.locator('.gallery__item.card');
  const productCount = await productList.count();
  expect(productCount).toBeGreaterThan(0);

  for (let i = 0; i < productCount; i++) {
    const productName = await productList.nth(i).locator('.card__title').innerText();
    expect(productName).not.toBe('');
    const productPrice = await productList.nth(i).locator('.card__price').innerText();
    expect(productPrice).not.toBe('');
  }
  
  const firstProduct = productList.nth(0);
  const firstProductName = await firstProduct.locator('.card__title').innerText();
  const firstProductPrice = await firstProduct.locator('.card__price').innerText();
  await firstProduct.click();
  const addToBasketButton = page.locator('#modal-container.modal_active .card__button');
  await addToBasketButton.waitFor({ state: 'visible', timeout: 10000 });
  await addToBasketButton.click(); 
  const basketCounter = await page.locator('.header__basket-counter').innerText();
  expect(basketCounter).toBe('1'); 
  
  const basketButton = page.locator('.header__basket');
  await basketButton.click();
  const basketItemName = await page.locator('#modal-container.modal_active .basket__item .card__title').innerText();
  const basketItemPrice = await page.locator('#modal-container.modal_active .basket__item .card__price').innerText();
  expect(basketItemName).toBe(firstProductName);
  expect(basketItemPrice).toBe(firstProductPrice);
  const totalBasketPrice = await page.locator('#modal-container.modal_active .basket__price').innerText();
  expect(totalBasketPrice).toBe(firstProductPrice);

   const closeButton = page.locator('#modal-container.modal_active .modal__close');
   await closeButton.click();
});

