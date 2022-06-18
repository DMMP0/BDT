public class MapDeserializer implements Deserializer<Map> {

    @Override
    public void close() {

    }

    @Override
    public void configure(Map config, boolean isKey) {

    }

    @Override
    public Map deserialize(String topic, byte[] message) {
        ByteArrayInputStream bis = new ByteArrayInputStream(message);
        ObjectInput in = null;
        try {
            in = new ObjectInputStream(bis);
            Object o = in.readObject();
            if (o instanceof Map) {
                return (Map) o;
            } else
                return new HashMap<String, String>();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                bis.close();
            } catch (IOException ex) {
            }
            try {
                if (in != null) {
                    in.close();
                }
            } catch (IOException ex) {
                // ignore close exception
            }
        }
        return new HashMap<String, String>();
    }
}
