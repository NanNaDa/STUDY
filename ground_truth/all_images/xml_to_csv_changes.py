import os

def main():
	for folder in ['train', 'test']:
	    image_path = os.path.join(os.getcwd(), ('/' + folder))
	    xml_df = xml_to_csv(image_path)
	    xml_df.to_csv(('/' + folder + '_labels.csv'), index=None)
	    print('Successfully converted xml to csv.')

