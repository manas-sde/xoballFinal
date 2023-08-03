import { render, fireEvent } from "@testing-library/svelte";
import ToggleParagraph from "./+page.svelte";

describe("ToggleParagraph component", () => {
  it("should not show paragraph at start", () => {
    const { queryByText } = render(ToggleParagraph);
    const paragraph = queryByText("This is a paragraph.");
    expect(paragraph).not.toBeVisible();
  });

  it("should show paragraph after clicking the anchor element once", async () => {
    const { getByText, queryByText } = render(ToggleParagraph);
    const anchor = getByText("Click me");
    fireEvent.click(anchor);
    const paragraph = await queryByText("This is a paragraph.");
    expect(paragraph).toBeVisible();
  });

  it("should hide paragraph after clicking the anchor element twice", async () => {
    const { getByText, queryByText } = render(ToggleParagraph);
    const anchor = getByText("Click me");
    fireEvent.click(anchor);
    fireEvent.click(anchor);
    const paragraph = await queryByText("This is a paragraph.");
    expect(paragraph).not.toBeVisible();
  });
});
