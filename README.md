{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a7ce2c14-b549-449c-ae63-9451b914ad99",
   "metadata": {},
   "source": [
    "# Main"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "43da46d3-1e15-4aa2-be8f-d05b722aed3a",
   "metadata": {},
   "outputs": [],
   "source": [
    " # Task 1\n",
    " \"\"\"import json\n",
    "\n",
    " with open('data.json', 'r') as f:\n",
    "     lst = json.load(f)\n",
    " div3 = [num for num in lst if num % 3 == 0]\n",
    " print(sum(div3) / len(div3))\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0fde7ae2-2866-413a-a6e2-de3bb65c581f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Task 2\n",
    " \"\"\"dict1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}\n",
    " dict2 = {}\n",
    " for i in dict1.values():\n",
    "     dict2[i] = len(i)\n",
    " print(dict2)\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "52a3b498-9e9b-48ad-b29f-907361226477",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Task 3\n",
    " \"\"\"d = {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]}\n",
    "\n",
    " for a,s in d.items():\n",
    "     d[a] = [i for i in s if i % 2 != 0]\n",
    " print(d)\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "36cdd13c-0abe-4f31-ba12-33232a05d378",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
