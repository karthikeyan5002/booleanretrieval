import argparse
import timeit
import streamlit as st
from ir_system import IRSystem
import numpy as np
import pandas as pd
# docs1 = ["Ice-cream, Mango, Litchi",
#         "Hockey, Cricket, Sport",
#         "Ice-cream, Litchi, Mango, Chocolate",
#         "Ice-cream, Milk-shake, Water",
#         "Nice, Good, Cute"]
st.write("## Boolean Information Retrieval System✨")
st.write("### Enter the documents below👇")
col1, col2, col3 = st.columns(3)
with col1:
    d1 = st.text_input("Enter the first document", "Ice-cream, Mango, Litchi")
    d4 = st.text_input("Enter the fourth document",
                       "Ice-cream, Milk-shake, Water")
with col2:
    d2 = st.text_input("Enter the second document", "Hockey, Cricket, Sport")
    d5 = st.text_input("Enter the fifth document", "Nice, Good, Cute")
with col3:
    d3 = st.text_input("Enter the third document",
                       "Ice-cream, Litchi, Mango, Chocolate")

docs = [d1, d2, d3, d4, d5]

# documents = ["Ice-cream, Mango, Litchi", "Hockey, Cricket, Sport",
#              "Ice-cream, Litchi, Mango, Chocolate", "Ice cream, Milk-shake, Water", "Nice, Good, Cute"]
# vocab = ["Ice-cream", "Mango", "Litchi", "Hockey", "Cricket", "Sport",
#          "Chocolate", "Milk-shake", "Water", "Nice", "Good", "Cute"]
words = [word.lower() for doc in docs for word in doc.split(', ')]

# Add the words to a set to get the unique vocabulary
vocab = words

td_matrix = np.zeros((len(vocab), len(docs)))
for i, term in enumerate(vocab):
    for j, doc in enumerate(docs):
        if term.lower() in doc.lower():
            td_matrix[i][j] = 1

# print the transposed incidence matrix table
print("Transposed incidence matrix table:")
rows = []
for i in range(len(vocab)):
    row = {'term': vocab[i]}
    for j in range(len(td_matrix[i])):
        col_name = 'd{}'.format(j+1)
        row[col_name] = int(td_matrix[i][j])
    rows.append(row)

# Create the dataframe from the list of dictionaries
df = pd.DataFrame(rows)

# Print the dataframe
df1 = df.T


stop_words = ['is', 'a', 'for', 'the', 'of']


def parse_args():
    parser = argparse.ArgumentParser(
        description='Information Retrieval System Configuration')
    return parser.parse_args()


st.write(docs)
st.write("#### the transposed incidence matrix table:")
st.table(df1)
if d5:
    args = parse_args()
    ir = IRSystem(docs, stop_words=stop_words)

    query = st.text_input("Enter the query", "Good AND (Mango OR Litchi)")
    start = timeit.default_timer()
    results = ir.process_query(query)
    stop = timeit.default_timer()
    if st.button("Show Results"):
        st.write('#### Processing time: {:.5} secs'.format(stop - start))
        st.write('\nDoc IDS: ')
        print(results)
        try:
            st.write("#### {0}".format(results))
        except TypeError as e:
            st.write("#### No results found")
    print()

# def main():
#     args = parse_args()
#     ir = IRSystem(docs, stop_words=stop_words)
#     while True:
#         query = input('Enter boolean query: ')

#         start = timeit.default_timer()
#         results = ir.process_query(query)
#         stop = timeit.default_timer()
#         if results is not None:
#             print('Processing time: {:.5} secs'.format(stop - start))
#             print('\nDoc IDS: ')
#             print(results)
#         print()


# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt as e:
#         print('EXIT')
