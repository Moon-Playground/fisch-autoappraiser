# 📖 How to Use AutoAppraiser

AutoAppraiser automates the tedious process of appraising fish in **Fisch (Roblox)** by using high-speed screen capture and OCR to detect specific mutations.

---

## 🛠️ 1. Initial Setup

1.  **Open AutoAppraiser**: Launch the application.
2.  **Select Mutations**: Navigate to the **Mutations** tab and check the ones you want to keep (e.g., *Abyssal*, *Celestial*, *Mythical*). 
    *   *The automation will stop as soon as any selected mutation is detected.*
3.  **Configure Fish Slot**: Go to the **Settings** tab and set the **Fish Slot** (1-9) to match your in-game hotbar position for the fish. Click **Save Settings**.

---

## 🎯 2. Defining the Capture Area

Defining a precise capture area is the most important step for high accuracy.

1.  **Manual Appraisal**: Perform a manual appraisal in-game. **Keep the npc dialog open.**
2.  **Show Overlay**: Press `F3` to toggle the blue capture box.
3.  **Position & Resize**: Drag and resize the box to cover ONLY the mutation text area.
    *   **Pro Tip**: Make sure the text background is not green, as it can confuse the OCR.
4.  **Save Area**: Press `F3` again to hide the box and save the position.

![Capture Box Example](https://github.com/Moon-Playground/fisch-autoappraiser/blob/main/.github/assets/capture_box.png)  
*(Recommended camera position and box placement)*

---

## 🚀 3. Starting the Automation

1.  **Equip Requirements**: Ensure you have enough currency for appraisals and the fish is in the correct hotbar slot.
2.  **Mouse Placement**: Move your mouse cursor over the **Appraise** button in the in-game dialog.
3.  **Start Loop**: Press `F4`.
    *   The Status will change to **Active** (Green).
    *   The app will automatically press the slot key, click the button, and scan the result.

![Mouse Position Example](https://github.com/Moon-Playground/fisch-autoappraiser/blob/main/.github/assets/mouse_position.png)  
*(Keep your cursor over the button before starting)*

4.  **Mutation Detection**: If the mutation is detected, the app will show a popup with the mutation name. just like the image below:

![Mutation Detected](https://github.com/Moon-Playground/fisch-autoappraiser/blob/main/.github/assets/mutation_detected.png)

---

## ⌨️ 4. Hotkeys Reference

| Key | Action | Description |
| :--- | :--- | :--- |
| **`F2`** | `Test Capture` | Takes a snapshot and shows you exactly what the OCR engine "sees". |
| **`F3`** | `Toggle Overlay` | Shows/Hides the blue capture box for configuration. |
| **`F4`** | `Start/Stop` | Toggles the automation on or off. |
| **`F5`** | `Force Exit` | Immediately closes the application and stops all loops. |

*(Hotkeys can be customized in the **Hotkeys** tab.)*

---

## 💡 5. Tips & Troubleshooting

-   **OCR failing?**: Use `F2` to debug. If the "OCR Result" in the popup doesn't match the text in-game, try making the capture box slightly larger or moving it a few pixels.
-   **Wrong Mutation detected?**: The app uses fuzzy matching to handle OCR errors. If it's stopping on the wrong mutation, try refining the capture region for a cleaner background.
-   **Performance**: If the game lags, try switching the **Capture Mode** in Settings between `DXCAM` and `MSS`.
-   **Save your work**: Always click **Save Settings** or **Save & Reload Hotkeys** after making changes in those tabs.
