import unittest
from unittest.mock import patch, Mock
import asyncio
from stablediffusion import StableDiffusion


class TestStableDiffusionIntegration(unittest.IsolatedAsyncioTestCase):

    async def test_stable_diffusion_success(self):
        with patch("requests.post") as mock_post:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.content = b"image data"
            mock_post.return_value = mock_response

            response = await StableDiffusion.get_stable("Test prompt")
            self.assertEqual(response, b"image data", "Должен возвращаться контент изображения")

    async def test_stable_diffusion_api_error(self):
        with patch("requests.post") as mock_post:
            mock_response = Mock()
            mock_response.status_code = 401
            mock_response.content = b""
            mock_post.return_value = mock_response

            response = await StableDiffusion.get_stable("Test prompt")
            self.assertIsNone(response, "При ошибке должен возвращаться None")

    async def test_async_behavior(self):
        with patch("requests.post") as mock_post:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.content = b"image data"
            mock_post.return_value = mock_response

            response = await asyncio.gather(
                StableDiffusion.get_stable("Prompt 1"),
                StableDiffusion.get_stable("Prompt 2")
            )
            self.assertEqual(len(response), 2, "Должны получить два результата")
            self.assertEqual(response[0], b"image data")
            self.assertEqual(response[1], b"image data")

    async def test_missing_api_key(self):
        with patch("stablediffusion.getenv", return_value=None):
            response = await StableDiffusion.get_stable("Test prompt")
            self.assertIsNone(response, "Должен возвращаться None, если ключ API отсутствует")

    async def test_invalid_prompt(self):
        response = await StableDiffusion.get_stable("")
        self.assertIsNone(response, "Должен возвращаться None для пустого промпта")


if __name__ == "__main__":
    unittest.main()
