
import asyncio
from notebooklm_mcp.api_client import NotebookLMClient
from notebooklm_mcp.auth import load_cached_tokens

async def main():
    tokens = load_cached_tokens()
    if not tokens:
        print("Error: No cached tokens found. Run `notebooklm-mcp-auth`.")
        return

    client = NotebookLMClient(
        cookies=tokens.cookies,
        csrf_token=tokens.csrf_token,
        session_id=tokens.session_id
    )
    try:
        notebooks = client.list_notebooks()
        print(f"Success! Found {len(notebooks)} notebooks.")
        for nb in notebooks[:5]:
            print(f"- {nb.title} ({nb.id})")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
