import { test, expect } from '@playwright/test';

test('Add first product to basket and complete the order', async ({ page }) => {
  await page.goto('http://localhost:8080/');
  
  await page.waitForSelector('.gallery__item.card', { timeout: 5000 });

  const productList = page.locator('.gallery__item.card');
  const firstProduct = productList.nth(0);
  const firstProductName = await firstProduct.locator('.card__title').innerText();
  const firstProductPrice = await firstProduct.locator('.card__price').innerText();
  await firstProduct.click();

  const addToBasketButton = page.locator('#modal-container.modal_active .card__button');
  await addToBasketButton.waitFor({ state: 'visible', timeout: 5000 });
  await addToBasketButton.click();

  const basketCounter = await page.locator('.header__basket-counter').innerText();
  expect(basketCounter).toBe('1');

  const basketButton = page.locator('.header__basket');
  await basketButton.click();

  const basketItemName = await page.locator('#modal-container.modal_active .basket__item .card__title').innerText();
  const basketItemPrice = await page.locator('#modal-container.modal_active .basket__item .card__price').innerText();
  expect(basketItemName).toBe(firstProductName);
  expect(basketItemPrice).toBe(firstProductPrice);

  const checkoutButton = page.locator('#modal-container.modal_active .basket__button');
  await checkoutButton.waitFor({ state: 'visible', timeout: 5000 });
  await checkoutButton.click();

  const addressInput = page.locator('#modal-container.modal_active input[placeholder="Введите адрес"]');
  await addressInput.waitFor({ state: 'visible', timeout: 5000 });

  const onlinePaymentButton = page.locator('#modal-container.modal_active .order__buttons .button[name="card"]');
  await onlinePaymentButton.click();
  await addressInput.fill('г. Санкт-Петербург, ул. Ломоносова, д. 9');

  const nextButton = page.locator('#modal-container.modal_active .button.order__button');
  await expect(nextButton).toBeEnabled();
  await nextButton.click();

  const emailInput = page.locator('#modal-container.modal_active input[placeholder="Введите Email"]');
  const phoneInput = page.locator('#modal-container.modal_active input[placeholder="+7 ("]');
  await emailInput.fill('yaroslav.kolsanov@mail.ru');
  await phoneInput.fill('+7 (953) 011-00-07');
  const payButton = page.locator('#modal-container.modal_active .button:has-text("Оплатить")');
  await expect(payButton).not.toBeDisabled(); 

  await payButton.click();

  const successMessage = page.locator('#modal-container.modal_active .order-success__title');
  await expect(successMessage).toHaveText('Заказ оформлен');
});

