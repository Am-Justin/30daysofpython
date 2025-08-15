import numpy as np

np_normal_dis = np.random.normal(5, 0.5, 100)
np_normal_dis

two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])

print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ',two_dimension_array.mean())
print('median: ', two_dimension_array.median())
print('sd: ', two_dimension_array.std())


print(two_dimension_array)
print('Column with minimum: ', np.amin(two_dimension_array,axis=0))
print('Column with maximum: ', np.amax(two_dimension_array,axis=0))
print('=== Row ==')
print('Row with minimum: ', np.amin(two_dimension_array,axis=1))
print('Row with maximum: ', np.amax(two_dimension_array,axis=1))

