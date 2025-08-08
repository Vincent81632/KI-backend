import { Link } from 'expo-router'
import { Text, View } from 'react-native'

export default function EinstellungenScreen() {
    return (
        <View>
            <Link href="/fragebogen" style = {{ marginTop: 200}}>
                <Text style={{ color: 'blue' }}>Fragebogen</Text>
            </Link>
        </View>
    )
}
